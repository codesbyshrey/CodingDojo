// AddAvailability.js handleSubmit for payload w/ days/destination/location
// Have to fix location issue firsthand for the rest of the availability issues to follow suit
// location_1 or location_1_id or location_1_id_id
// CHECK PGADMIN DATA TABLE NAMES FOR CORROBORATION

const handleSubmit = async () => {
     let data = handleValidation();
     //if it is an alert box then data is undefined
     // console.log("validated data is", data);
     if (!data) {
          //if just the last empty array
          if (workHourArray.length === 1) {
               return Alert.alert("Please save your work hours before going to the next screen");
          }
          if (workHourArray.length > 1) {
               for (let i = 0; i < workHourArray.length - 1; i++) {
                    if (
                         !workHourArray[i]["location"] ||
                         !locationDropdownOption.includes(workHourArray[i]["location"])
                    ) {
                         return Alert.alert(
                              "please select the location for each pending item"
                         );
                    }
               }
          }
          console.log(
               "final result is",
               workHourArray,
               "!!!",
               locationArray,
               "@@@",
               locationDropdownOption);
     }
     // const daysArray = workHourArray.map((entry) => entry
     const daysArray = workHourArray.map((entry) => entry["days"]);
     // daysArray will contain an array of "days" values from each element in locationArray

     const payload = {
          expert_id: profID,
          location_1: locationArray[0]["location"],
          // Assuming you want to use the first location entry
          destination_type_personal: locationArray[0]["personal"],
          // Assuming you want to use the first location entry
          destination_type_business: locationArray[0]["business"],
          // Assuming you want to use the first location entry
          mon: daysArray.includes("Mon"),
          tue: daysArray.includes("Tue"),
          wed: daysArray.includes("Wed"),
          thu: daysArray.includes("Thu"),
          fri: daysArray.includes("Fri"),
          sat: daysArray.includes("Sat"),
          sun: daysArray.includes("Sun"),
          work_hour_start: workHourArray[0]["startTime"],
          work_hour_end: workHourArray[0]["endTime"],
          // Assuming you want to use the end time from the first location entry
          on_site: workHourArray[0]["on_site"],
          // Assuming you want to use the on_site value from the first location entry
          off_site: workHourArray[0]["off_site"],
          // Assuming you want to use the off_site value from the first location entry
     }
          .then(() => {
               navigation.push("Add Cancellation Intro", {
                    market: industryType,
               });
          })
          .catch((error) => {
               console.error("Error Saving Availability:", error);
          });

};

