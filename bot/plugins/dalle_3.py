from typing import Dict
from .plugin import Plugin
from dotenv import load_dotenv
import os
import logging
import openai

load_dotenv()


class DallE3(Plugin):
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_source_name(self) -> str:
        return "DallE3"

    def get_spec(self) -> [Dict]:
        return [{
            "name": "generate_image",
            "description": "Generates an image based on a prompt",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "maxLength": 1000,
                        "description": "A detailed description of the image in English language, up to"
                                       "1000 characters, examples:"
                                       "A photo of Charles Babbage building a robot by Philippe Halsman, setting in an engineer workshop, canon lens, shot on dslr 64 megapixels sharp focus, vintage photography, Victorian colorised,character design by mark ryden and pixar and hayao miyazaki"
                                       "Cute small rabbit sitting in a movie theater eating popcorn watching a movie ,unreal engine, cozy indoor lighting, art station, detailed, digital painting,cinematic,character design by mark ryden and pixar and hayao miyazaki, unreal 5, daz, hyperrealistic, octane render"

                    },
                    "imageStyle": {
                        "type": "string",
                        "enum": ["vivid", "natural"],
                        "description": "The style of the generated image"
                    }
                },
                "required": ["prompt", "imageStyle"]
            }

        }]

    async def execute(self, function_name, helper, **kwargs) -> Dict:
        try:
            response = await self.client.images.generate(
                prompt=kwargs['prompt'],
                n=1,
                model=os.getenv("image_model", "dall-e-3"),
                # TODO let the user choose the quality
                quality='hd',
                style=kwargs['imageStyle'],
                size='1024x1024'
            )

            if len(response.data) == 0:
                logging.error(f'No response from DallE: {str(response)}')
                raise Exception(
                    f"⚠️ _error has been happened._ "
                )

            return {"image": response.data[0].url, "size": os.getenv("image_size", "1024x1024")}
        except Exception as e:
            raise Exception(f"⚠️ _Something wrong happened._ ⚠️\n{str(e)}") from e
