---
layout: default
title: 分野別記事
permalink: /categories/
---
# 分野別記事
{% assign cats = site.categories | sort %}
{% for cat in cats %}
## {{ cat[0] }}
<ul>{% for post in cat[1] %}<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>{% endfor %}</ul>
{% endfor %}
