class Formatter:
    def format_query_results(self, results):
        formatted_results = [f"{result[1]} {result[2]} {result[3]} {result[4]}" for result in results]
        return "\n".join(formatted_results)