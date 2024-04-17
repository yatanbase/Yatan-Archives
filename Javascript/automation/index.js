const JSON = require("jsonfile");
const moment = require("moment");
const File_path = "./data.json";
const simpleGit = require("simple-git");

// Set the target date to April 20th of the current year
const DATE = moment().startOf('year').month('April').date(20).format();

// Function to make a commit with specified x and y values
const makeCommit = (x, y) => {
    const DATE_WITH_OFFSET = moment(DATE).add(x, 'weeks').add(y, 'days').format(); // Adjusted date calculation with x and y

    const data = {
        date: DATE_WITH_OFFSET
    };

    console.log(DATE_WITH_OFFSET);

    JSON.writeFile(File_path, data, () => {
        simpleGit().add([File_path]).commit(DATE_WITH_OFFSET, {'--date': DATE_WITH_OFFSET}).push();
    });
};

// Calling makeCommit function with x and y values
makeCommit(3, 3); // Example values for x and y
