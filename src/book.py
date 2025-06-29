import streamlit as st
import yaml


def load_books_from_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def render_books_grid(books_list, col_count):
    for i in range(0, len(books_list), col_count):  # Process books per row
        cols = st.columns(col_count)  # Create columns
        for j, book in enumerate(
            books_list[i : i + col_count]
        ):  # Add books into the row
            with cols[j]:  # Assign each book to a column
                # Display date or "읽는 중" based on WIP status
                if book.get("wip", False):
                    status_html = '<div style="color: #007bff; font-weight: bold;">읽는 중</div>'  # Blue color for WIP
                else:
                    status_html = f'<div style="color: gray;">{book["date"]}</div>'

                st.markdown(
                    f"""
                <img src="{book["cover_url"]}" style="height: 230px; border-radius: 0.5rem; margin-bottom: 1rem;">
                <div style="height: 3rem; font-weight: bold;">{book["title"]}</div>
                <div style="margin-top: 0.5rem;">
                    {"<br />".join(book["author"]) if isinstance(book["author"], list) else book["author"]}
                </div>
                {status_html}
                """,
                    unsafe_allow_html=True,
                )
                st.markdown("")


data = load_books_from_yaml("src/data.yaml")
books = data["books"]

# order by date desc
books = sorted(books, key=lambda x: x["date"], reverse=True)

st.title("📚 독서기록장")
st.html(
    f"""
    총 독서 권수: <b>{len([book for book in books if not book.get("wip", False)])}</b>
    """
)

col_count = 4


# Render all books in a single grid
render_books_grid(books, col_count)
