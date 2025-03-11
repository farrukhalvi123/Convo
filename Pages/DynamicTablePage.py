from selenium.webdriver.common.by import By


class DynamicTablePage():
    def __init__(self, browser):
        self.browser = browser
        self.tableid = "table1"
        self.heading_tag = "thead"
        self.body_tag = "tbody"
        self.table_rows = "tr"
        self.cells = "td"

    def get_table_data(self):
        try:
            table = self.browser.find_element(By.ID, self.tableid)
            header = table.find_element(By.TAG_NAME, self.heading_tag)  # Get Heading
            body = table.find_element(By.TAG_NAME, self.body_tag)  # Getting Body text
            headers = [th.text.strip() for th in header.find_elements(By.TAG_NAME, "th")]

            # Getting all rows data
            data = [headers]
            for row in body.find_elements(By.TAG_NAME, self.table_rows):
                cells = row.find_elements(By.TAG_NAME, self.cells)
                row_data = [cell.text.strip() for cell in cells]
                data.append(row_data)
            print(data)
            return data
        except Exception as e:
            print(f"Error: Unable to locate table with ID {self.tableid}")
            raise

    def verify_table_data(self,first_name,last_name):
        try:
            table_data = self.get_table_data()  # Call the method properly

            for row in table_data[1:]:  # Skip header row
                if last_name in row and first_name in row:
                    print(f"Assertion Passed: {first_name} {last_name} found in table.")
                    return True

        except Exception as e:
            print(f"Assertion Failed: {first_name} {last_name} not found in table.")
            return False






