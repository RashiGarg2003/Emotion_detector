import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=headers)
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        
        # Adjust the keys based on the actual response structure
        emotion_predictions = formatted_response.get('emotionPredictions', [{}])[0].get('emotion', {})
         anger = emotion_predictions.get('anger', 0)
        disgust = emotion_predictions.get('disgust', 0)
        fear = emotion_predictions.get('fear', 0)
        joy = emotion_predictions.get('joy', 0)
        sadness = emotion_predictions.get('sadness', 0)
        
        # Find the dominant emotion
        emotions = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        
        dominant_emotion = max(emotions, key=emotions.get)
         return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {"error": "Failed to get a valid response from the server."}
