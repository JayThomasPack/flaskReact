from flask import Blueprint, request, jsonify
from services.scraper import scrape_url
from services.huggingface import generate_questionnaire
from services.database import save_questionnaire

urls_bp = Blueprint('urls', __name__)

@urls_bp.route('/urls', methods=['POST'])
def urls():
    data = request.get_json()
    url = data.get("urls")
    if not url:
        return jsonify({"error": "Invalid URL"}), 400
    
    try:
        scraped_data = scrape_url(url)
        print(scraped_data)
        questionnaire = generate_questionnaire(scraped_data)
        save_questionnaire(url, questionnaire)
        return jsonify({"result": questionnaire}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
