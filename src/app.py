from collections import Counter
from flask import Flask, request, jsonify
from wikipedia import wikipedia

app = Flask(__name__)

# In-memory storage for search history
search_history = []


# Endpoint for returning top frequent words
@app.route('/word-frequencies', methods=['GET'])
def get_word_frequencies():
    try:
        topic = request.args.get('topic')
        n = int(request.args.get('n', 10))
        result = wikipedia.summary(topic)
        counter = Counter(result.split())
        frequent_words = {}
        for (i, j) in counter.most_common(n):
            frequent_words[i] = j
        search_history.append({"topic": topic, "n": n, "frequent_words": frequent_words})
        return jsonify({'topic': topic, "frequent_words": frequent_words})
    except Exception as e:
        return jsonify({'error': str(e)})


# Endpoint for search history
@app.route("/search_history", methods=['GET'])
def get_search_history():
    return jsonify({"search_history": search_history})


if __name__ == '__main__':
    app.run(debug=True)
