# See sd_run.py for status and copyright release information

from sd_functions import allow_bots


# Check for various things before allowing a page edit
def ok_to_edit(page, title, description, username, existing_desc, existing_type, override_manual, override_embedded):
    if not page.exists():
        print(title + ' -   NO EDIT MADE: Page does not exist')
        return False
    if page.text == '':
        print(title + ' - NO EDIT MADE: Page has been blanked')
        return False
    if not allow_bots(page.text, username):
        print(title + ' - NO EDIT MADE: Bot is excluded via the Bots template')
        return False
    if description == existing_desc:
        print(title + f' - NO EDIT MADE: No change to "{description}"')
        return False
    # Don't edit if not allowed to change an existing description
    if not override_manual and existing_type == 'manual':
        print(title + ' - NO EDIT MADE: Page now has a manual description')
        return False
    if not override_embedded and existing_type == 'embedded':
        print(title + ' - NO EDIT MADE: Page now has an embedded description')
        return False
    # Unexpected error
    if title != page.title():
        print(title + f' - ERROR: page.title is "{page.title()}", but title from file is "{title}"')
        raise AssertionError
        return False

    #  **** MOTH UPDATE RUN ONLY  *********

    if existing_desc not in ('Species of moth', 'Genus of moths'):
        print(title + ' - NO EDIT MADE: Moth article has a non-bot description')
        return False


    return True
