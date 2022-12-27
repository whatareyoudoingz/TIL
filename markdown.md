# 마크다운 문법 정리

## **개념 정리**

### **마크다운**

> 특징
- **워드프로세서**는 다양한 서식과 구조를 지원하고, 문서에 즉각적으로 반응한다. 그러나 다른 프로그램으로 **호환**에 **제약**이 있고, 워드프로세스 상의 기능 활용해야함.
- **단순 텍스트** 문법으로 내용작성(최소한의 문법으로 구조화), **다양한 환경**에서 **활용**가능

> 활용 예시
- **README.md**
    - 오픈소스의 공식 문서 작성 또는 개인 프로젝트의 프로젝트 소개서 활용
    - 모든 페이지에 README.md를 넣어 문서를 바로 볼 수 있도록 활용
- **정적사이트생성기 기반 블로그**
    - Jekyll, gatsby, Hugo, hexo 등으로 작성된 마크다운을 HTML, CSS,JS 파일 등으로 변환하고, Github pages 기능을 통해 무료 호스팅이 가능함.


> [참고사이트](https://www.markdownguide.org/cheat-sheet/)  
<br/>

---  
## **마크다운 사용법**  
<br/>

###  **제목(Heading)**
<br/>

# Hello
## Hello
### Hello

```python
# Hello
## Hello
### Hello
```
<br/>

---
### **굵게(Bold)**
<br/>

**굵게 text**

```python
 **굵게 text**
 ```
<br/>

---
### **기울임(Italic)**
<br/>

*기울임 text*
```python
*기울임 text*
```
<br/>

---
### **인용문(Blockquotes)**
<br/>

> blockquote

```python
> blockquote
```
<br/>

---
### **정렬된 목록**
<br/>

1. First item
2. Second item
3. Third item

```python
1. First item
2. Second item
3. Third item
```
<br/>

---
### **정렬되지 않은 목록**
<br/>

- First item
- Second item
- Third item

```python
- First item
- Second item
- Third item
```
<br/>

---
### **암호**
<br/>

`code`

```python
`code`
```
<br/>

---
### **수평선**
<br/>

---
***
___

```python
___
***
---
```
<br/>

---
### **링크**
<br/>

[title](https://www.example.com)

```python
[문자열](URL)
[title](https://www.example.com)
```
<br/>

---
### **영상**
<br/>

![alt text](image.jpg)

```python
![문자열](URL)
![alt text](image.jpg)
````
<br/>

---
### **테이블(Table)**
<br/>

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
<br/>

---
### **울타리 코드 불록(Fenced Code Block)**
<br/>

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
<br/>

---
### **각주(Footnote)**
<br/>

Here's a sentence with a footnote. [^1]

**[^1]** 가 각주이다.
<br/>

---
### **제목 ID(Heading ID)**
<br/>

```python
### My Great Heading {#custom-id}
```
<br/>

---
### **정의 목록(Definition List)**
<br/>

term 
: definition

```python
term 
: definition
```
<br/>

---
### **취소선(Strikethrough)**
<br/>

~~The world is flat.~~

```python
~~The world is flat.~~
```
<br/>

---
### **작업 목록(Task List)**
<br/>

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

```python
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media
```
<br/>

---
### **이모티콘(Emoji)**
<br/>

That is so funny! :joy:

```python
That is so funny! :joy:
```
<br/>

---
### **강조(Highlight)**
<br/>

I need to highlight these ==very important words==.


```python
 I need to highlight these ==very important words==.
 ```
<br/>

---
### **아래 첨자**
<br/>

H~2~O

```python
H~2~O
 ```
<br/>

--- 
### **큰 첨자**
<br/>

X^2^

```python
X^2^
 ```
 <br/>

--- 
 ### 이 외의 다양한 관련 자료
 - [GitHub Flavored Markdown](https://github.github.com/gfm/)
 - [Mastering Markdown](https://docs.github.com/ko/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
 - [Markdown Guide](https://www.markdownguide.org/)