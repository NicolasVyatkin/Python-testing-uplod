class WorkWithInfo:

    def save_result_to_file(self, file, result):
        """function that saves info to file"""
        with open(file, "w") as file:
            for i in result:
                file.write(i+'::')
