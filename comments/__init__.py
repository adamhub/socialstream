def get_model():
    from .models import CComment
    return CComment

def get_form():
    from .forms import CCommentForm
    return CCommentForm