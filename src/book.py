import streamlit as st
import yaml


def load_books_from_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


data = load_books_from_yaml("src/data.yaml")
books = data["books"]

st.title("📚 Book Shelf")
st.html(
    f"""
    Reading list for jaehong21<br />
    Total books: <b>{len(books)}</b>
    """
)

# order by date desc
books = sorted(books, key=lambda x: x["date"], reverse=True)

# Render books as cards in a 4-column grid
col_count = 4
for i in range(0, len(books), col_count):  # Process books per row
    cols = st.columns(col_count)  # Create columns
    for j, book in enumerate(books[i : i + col_count]):  # Add books into the row
        with cols[j]:  # Assign each book to a column
            st.markdown(
                f"""
            <img src="{book['cover_url']}" style="height: 230px; border-radius: 0.5rem; margin-bottom: 1rem;">
            <div style="height: 3rem; font-weight: bold;">{book['title']}</div>
            <div style="margin-top: 0.5rem;">
                {"<br />".join(book['author']) if isinstance(book['author'], list) else book['author']}
            </div>
            <div style="color: gray;">{book['date']}</div>
            """,
                unsafe_allow_html=True,
            )
            st.markdown("")
