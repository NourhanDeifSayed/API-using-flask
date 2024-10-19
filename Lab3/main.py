from flask import Flask,request,jsonify

app=Flask(__name__)

books=[
    {"bookID":1 , "title":"bookone" , "author":"author one"},
    {"bookID":2 , "title":"book two" , "author":"author two"},
    {"bookID":3, "title":"book three" , "author":"author three"}
]


@app.route("/books", methods=["GET"])
def get_book_all():
    return jsonify(books),200




@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book=next((b for b in books if b ["bookID"]==book_id),None) 
    if book:
        return jsonify(book), 200  
    else:
        return jsonify({"error": "Book Not Found"}), 404


@app.route("/books", methods=["POST"])
def add_book():
    data=request.get_json()
    new_book={"id":len(books)+1,"title":data["title"],"author":data["author"]}
    books.append(new_book)
    return jsonify(new_book),201 




@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book=next((b for b in books if b ["bookID"]==book_id),None) 
    if book:
        data=request.get_json()
        book.update({"title":data.get("title",book["title"]) , "author":data.get("author",book["author"]) })
        return jsonify(book)
    return  jsonify({"error":"Book Not Found"}),404





@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["bookID"] != book_id]
    return jsonify({"message": "Book deleted"})


if __name__=="__main__":
    app.run(debug=True)