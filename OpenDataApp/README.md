This simple Python project visualizes wind power production in Finland on user selected date. It uses Fingrid's dataset "Wind power production -real-time data" which updates every 3 minutes, but the program calculates the averages for each hour for better visualization. The program can be used to get insights of wind power production in Finland and how it flutcuates between days.

The program is simple: the user needs to just give a date as an input and the program displays the bar chart of that day.

Before running, the personal API key must be obtained from Fingrid's website. The link https://data.fingrid.fi/en/instructions contains Fingrid's detailed instructions on how to obtain the API key. Once created, copy the API key and navigate to api.py -file and replace the placeholder in apiKey variable.

Before running use the command
pip install -r requirements.txt
to install the matplotlib

Run the program in the project folder using command 
python main.py 
and enter a date in the format YYYY/MM/DD. The program checks that the date is formatted correctly and an API key exists before making an API call.

Example run: Enter a date between 2014/01/01 and the current date in the format YYYY/MM/DD: 2025/12/12
Expected output: bar chart showing the average hourly wind power production in MW for the selected day