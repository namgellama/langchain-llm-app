css = """
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}

.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}

.chat-message .avatar {
  width: 20%;
}

.chat-message .avatar img {
  height: 78px; 
    width: 78px; 
    border-radius: 50%; 
    object-fit: cover;
}

.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
"""


bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://deladavid.com/cdn/shop/products/Screen_Shot_2017-09-20_at_4.27.43_PM_grande.png?v=1585635380">
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""


user_template = """
<div class="chat-message user">
    <div class="avatar">
        <img src="https://images.pexels.com/photos/91227/pexels-photo-91227.jpeg?auto=compress&cs=tinysrgb&w=600">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
"""
