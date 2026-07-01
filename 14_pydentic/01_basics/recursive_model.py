from pydantic import BaseModel
from typing import Optional, List

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()  # Rebuild the model to resolve forward references   

comment_data = Comment(
    id=1,
    content="This is a comment",
    replies=[
        Comment(id=2, content="This is a reply"),
        Comment(id=3, content="This is another reply", replies=[
            Comment(id=4, content="Nested reply")
        ])
    ]
)

print(comment_data)