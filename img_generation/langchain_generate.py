from typing import Optional, Dict

from langchain import OpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.tools import BaseTool
from langchain.tools.steamship_image_generation.tool import (
    ModelName,
    SUPPORTED_IMAGE_SIZES,
)
from langchain.tools.steamship_image_generation.utils import make_image_public
from langchain.utils import get_from_dict_or_env
from load_dotenv import load_dotenv
from pydantic import root_validator
from steamship import Steamship

load_dotenv()

llm = OpenAI(temperature=0)


class SteamshipImageGenerationTool(BaseTool):
    """Tool used to generate images from a text-prompt."""

    model_name: ModelName
    size: Optional[str] = "512x512"
    steamship: Steamship
    return_urls: Optional[bool] = False

    name = "GenerateImage"
    description = (
        "Useful for when you need to generate an image."
        "Input: A detailed text-2-image prompt describing an image"
        "Output: the UUID of a generated image"
    )

    @root_validator(pre=True)
    def validate_size(cls, values: Dict) -> Dict:
        if "size" in values:
            size = values["size"]
            model_name = values["model_name"]
            if size not in SUPPORTED_IMAGE_SIZES[model_name]:
                raise RuntimeError(f"size {size} is not supported by {model_name}")

        return values

    @root_validator(pre=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        steamship_api_key = get_from_dict_or_env(
            values, "steamship_api_key", "STEAMSHIP_API_KEY"
        )

        try:
            from steamship import Steamship
        except ImportError:
            raise ImportError(
                "steamship is not installed. "
                "Please install it with `pip install steamship`"
            )

        steamship = Steamship(
            api_key=steamship_api_key,
        )
        values["steamship"] = steamship
        if "steamship_api_key" in values:
            del values["steamship_api_key"]

        return values

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""

        image_generator = self.steamship.use_plugin(
            plugin_handle=self.model_name.value, config={"n": 1, "size": self.size}
        )

        task = image_generator.generate(text=query, append_output_to_file=True)
        task.wait()
        blocks = task.output.blocks
        if len(blocks) > 0:
            if self.return_urls:
                return make_image_public(self.steamship, blocks[0])
            else:
                return blocks[0].id

        raise RuntimeError(f"[{self.name}] Tool unable to generate image!")


tools_for_agent1 = [
    SteamshipImageGenerationTool(
        name="GenerateImage",
        description="Useful for when you need to generate an image.",
        model_name="dall-e",
        size="512x512",
        return_urls=True,
    ),
]

agent = initialize_agent(
    tools_for_agent1, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

prompt = """
    An eco-friendly computer from the 90s in the style of vaporwave
"""

image_url = agent.run(prompt)

print(image_url)
