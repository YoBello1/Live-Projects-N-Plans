pip install openai;

Authorization: Bearer OPENAI_API_KEY;

import os
import openai
openai.organization = "org-rfND5EDqxjXxQYUvlaHttRMj"
openai.api_key = os.getenv("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")
openai.Model.list()


