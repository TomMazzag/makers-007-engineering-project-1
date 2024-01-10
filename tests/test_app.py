from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository
from lib.user import User

"""
When I call GET /spaces
I get a list of spaces back
"""
def test_get_spaces(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/spaces")
    name_element = page.locator(".t-space-name")
    expect(name_element).to_have_text(
        ["Space1", "Space2", "Space3", "Space4", "Space5"]
    )
    description_element = page.locator(".t-space-description")
    expect(description_element).to_have_text(
        [
            "Example description 1",
            "Example description 2",
            "Example description 3",
            "Example description 4",
            "Example description 5",
        ]
    )
    price_element = page.locator(".t-space-price")
    expect(price_element).to_have_text(["£130.0" for _ in range(5)])

"""
When we create a new space
We see it in the spaces index
"""
def test_create_space(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/spaces")
    page.click("text=List a space")
    page.fill("input[name='name']", "Test Name")
    page.fill("input[name='description']", "Test Description")
    page.fill("input[name='price']", "100")
    # When log in functionality is developed, must include test for correct user_id
    page.click("text=List my space")
    name_element = page.locator(".t-space-name")
    expect(name_element).to_have_text(["Space1", "Space2", "Space3", "Space4", "Space5", "Test Name"])
    description_element = page.locator(".t-space-description")
    expect(description_element).to_have_text(["Example description 1", 
                                            "Example description 2", 
                                            "Example description 3", 
                                            "Example description 4", 
                                            "Example description 5",
                                            "Test Description"])
    price_element = page.locator(".t-space-price")
    expect(price_element).to_have_text(["£130.0" for _ in range(5)] + ["£100.0"])

"""
When we create a user
We see it in the users table
"""
def test_create_user(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/signup")

    page.fill("input[name=username]", "user6")
    page.fill("input[name=email]", "user6@user.com")

    page.click("text='submit'")

    repository = UserRepository(db_connection)

    users = repository.all()
    assert users == [
        User(1, "user1", "user1@user.com"),
        User(2, "user2", "user2@user.com"),
        User(3, "user3", "user3@user.com"),
        User(4, "user4", "user4@user.com"),
        User(5, "user5", "user5@user.com"),
        User(6, "user6", "user6@user.com"),
    ]


