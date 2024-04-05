import React, {useState, FormEvent, useEffect} from "react"

const ReadFileComponent = () => {
  const [persons, setPersons] = useState([]);
  const [page, setPage] = useState(1)
  const [indexOfLastPage, setIndexOfLastPage] = useState(1)
  
  const handleNextPage = () => {
    setPage(prevPage => prevPage + 1);
    console.log(page)
  };

  const handlePrevPage = () => {
    setPage(prevPage => Math.max(prevPage - 1, 1));
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://localhost:8000/read?page=${page}&size=100`);
        if (response.ok) {
          const data = await response.json();
          setPersons(data.items);
          setIndexOfLastPage(data.pages)
        } else {
          console.error('Failed to fetch data');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [page]);

  return (
    <div className="container mx-auto">
      <div className="overflow-x-auto">
        <table className="table-auto w-full">
          <thead>
            <tr className="bg-gray-800 text-white">
              <th className="px-4 py-2">Name</th>
              <th className="px-4 py-2">GovernmentId</th>
              <th className="px-4 py-2">Email</th>
              <th className="px-4 py-2">Debt Amount</th>
              <th className="px-4 py-2">Debt Due Date</th>
              <th className="px-4 py-2">Debt Id</th>
            </tr>
          </thead>
          <tbody>
            
              {persons.map(person => { return (
                <tr className="bg-white" key={person["debtId"]}>
                  <td className="border px-4 py-2">{person["name"]}</td>
                  <td className="border px-4 py-2">{person["governmentId"]}</td>
                  <td className="border px-4 py-2">{person["email"]}</td>
                  <td className="border px-4 py-2">{person["debtAmount"]}</td>
                  <td className="border px-4 py-2">{person["debtDueDate"]}</td>
                  <td className="border px-4 py-2">{person["debtId"]}</td>
                </tr>
              )})}
            
          </tbody>
        </table>
        <div className="flex justify-between mt-4">
                <button
                  onClick={handlePrevPage}
                  disabled={page === 1}
                  className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
                >
                  Previous Page
                </button>
                <button
                  onClick={handleNextPage}
                  disabled={page > indexOfLastPage}
                  className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
                >
                  Next Page
                </button>
              </div>
      </div>
    </div>
  );
};

export {ReadFileComponent};