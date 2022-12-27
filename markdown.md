# 마크다운 문법 정리

[참고사이트](https://www.markdownguide.org/cheat-sheet/)를 참고하였습니다.

## 제목(Heading)

# Hello
## Hello
### Hello

```python
# Hello
## Hello
### Hello
```

---
## 굵게(Bold)
**굵게 text**

```python
 **굵게 text**
 ```

---
## 기울임(Italic)

*기울임 text*
```python
*기울임 text*
```

---
## 인용구
> blockquote

```python
> blockquote
```

---
## 정렬된 목록

1. First item
2. Second item
3. Third item

```python
1. First item
2. Second item
3. Third item
```

---
## 정렬되지 않은 목록

- First item
- Second item
- Third item

```python
- First item
- Second item
- Third item
```
---
## 암호

`code`

```python
`code`
```

---
## 가로줄

---

```python
---
```


---
## 링크

[title](https://www.example.com)

```python
[title](https://www.example.com)
```

---
## 영상

![alt text](image.jpg)

```python
![alt text](image.jpg)
````

---
## 테이블(Table)

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

```python
| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |
```

---
## 울타리 코드 불록(Fenced Code Block)

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

```python
```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
```

---
## 각주(Footnote)

Here's a sentence with a footnote. [^1]

**[^1]** 가 각주이다.

---
## 제목 ID(Heading ID)

```python
### My Great Heading {#custom-id}
```

---
## 정의 목록(Definition List)

term 
: definition

```python
term 
: definition
```

---
## 취소선(Strikethrough)
~~The world is flat.~~

```python
~~The world is flat.~~
```

---
## 작업 목록(Task List)

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

```python
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```

---
## 이모티콘(Emoji)

That is so funny! :joy:

```python
That is so funny! :joy:
```
---
## 강조(Highlight)

I need to highlight these ==very important words==.


```python
 I need to highlight these ==very important words==.
 ```

---
## 아래 첨자

H~2~O

```python
H~2~O
 ```

---
## 큰 첨자
X^2^

```python
X^2^
 ```