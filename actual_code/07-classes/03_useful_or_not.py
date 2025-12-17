item = {
    "title": "Election results",
    "status": "approved",
    "editor": "Sam"
}

def publish(item):
    if item["status"] != "approved":
        raise ValueError("Cannot publish yet")
    item["status"] = "published"

publish(item)
print(item)

class EditorialItem:
    def __init__(self, title, editor):
        self.title = title
        self.editor = editor
        self.status = "draft"

    def approve(self):
        self.status = "approved"

    def publish(self):
        if self.status != "approved":
            raise ValueError("Cannot publish yet")
        self.status = "published"

article = EditorialItem("AI is taking over the world", "Simon")
print(article.status)

article.approve()
article.publish()

print(article.status)