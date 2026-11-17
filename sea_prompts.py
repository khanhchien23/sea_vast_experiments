"""Sea-only prompts shared by training and inference."""
SEA_CLASSES = (
    "Sea.ArleighBurke", "Sea.Buyan", "Sea.GeraldFord", "Sea.Gorshkov",
    "Sea.Independence", "Sea.Kilo", "Sea.Kirov", "Sea.Molniya",
    "Sea.Nanuchka", "Sea.OsaII", "Sea.Ticonderoga", "Sea.Type002.Shandong",
    "Sea.Type022.Houbei", "Sea.Type051B.Luhai", "Sea.Type053H3.JiangweiII",
    "Sea.Type054A.JiangkaiII", "Sea.Type055.Renhai", "Sea.TypeAsahi",
    "Sea.TypeChengKung", "Sea.TypeKangDing", "Sea.Wasp",
)
DIRECT_SYSTEM = (
    "Classify the naval vessel in the image into exactly one of these classes: "
    + ", ".join(SEA_CLASSES)
    + ". Return only <answer>Exact_Class_Name</answer>."
)
DIRECT_USER = "Inspect the image and return only the exact Sea class in <answer>...</answer>."
SYSTEM_PROMPT = """You are an expert military analyst specializing in fine-grained naval vessel recognition.
Your task is to inspect the image and classify the vessel into EXACTLY ONE of these 21 target classes:
%s
Use only the exact class spelling from this list. Use the required format:
<think>
1. Viewpoint & Environment: ...
2. Coarse Category: ...
3. Fine-Grained Visual Features: ...
4. Disambiguation & Conclusion: ...
</think>
<answer>Exact_Class_Name</answer>""" % ", ".join(SEA_CLASSES)
USER_PROMPT = ("Inspect this military naval vessel carefully. Provide a structured 4-step visual analysis "
               "inside <think>...</think> and conclude with the exact class label inside "
               "<answer>...</answer>.")

