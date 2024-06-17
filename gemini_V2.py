import time

# hihihihihihhi
import google.generativeai as genai

genai.configure(api_key="AIzaSyCXCXxAcCQKxv-VAm7E0UnTNINXf3svPew")

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]
prompt = []
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)
convo = model.start_chat(history=[])


def model_response(text):
    data = {
        "role": "model",  # 指定角色為模型 (model)
        "parts": [{"text": f"{text}"}],  # 文字內容包含在 "text" 欄位
    }
    return data


# 使用者輸入函式 (user_word)
def user_word(text):
    data = {
        "role": "user",  # 指定角色為使用者 (user)
        "parts": [{"text": f"{text}"}],  # 文字內容包含在 "text" 欄位
    }
    return data


while True:
    # 獲取使用者輸入 (user_input)
    user_input = input("請問您想說什麼？輸入 'end' 結束對話\n")
    if user_input.lower() == "end":  # 不分大小寫比較輸入是否為 "end"
        print("對話結束")
        break  # 退出迴圈
    user_input = user_word(user_input)
    prompt.append(user_input)
    response = model.generate_content(prompt)
    print(response.text)
    model_output = model_response(response.text)
    prompt.append(model_output)
    time.sleep(1)
