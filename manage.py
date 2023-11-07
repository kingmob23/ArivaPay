from app import create_app, db

app = create_app()

@app.cli.command("init_db")
def init_db_command():
    """Create database tables from sqlalchemy models."""
    db.create_all()
    print("Initialized the database.")

if __name__ == '__main__':
    app.run()
