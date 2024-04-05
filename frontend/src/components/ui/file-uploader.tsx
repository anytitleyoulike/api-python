import {useState } from "react";

const FileUploader = () => {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  
  const handleFileChange = (e: any) =>  {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }

  }
  const handleSubmit = async (event: any) => {
    setLoading(true)
    event.preventDefault()
    if (!file) {
        alert("Please select a .csv file.")
        return;
    }
    const formData = new FormData()
    formData.append("files", file)
    try {
       await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData
      });
      alert("File uploaded successfully!")
      window.location.reload()
      
      return true;
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('An error occurred while uploading the file.');
    } finally {
      setLoading(false)
    }

}

  return (<div className="flex items-center justify-center bg-gray-100">
  <div className="max-w-md bg-white p-8 rounded shadow-md">
    <h2 className="text-2xl font-bold mb-4">Upload CSV File</h2>
    <form onSubmit={handleSubmit} onChange={handleFileChange} className="space-y-4" encType="multipart/form-data">
      <div>
        <label htmlFor="csvFile" className="block font-medium">Choose CSV File</label>
        <input type="file" id="csvFile" name="files" className="mt-1 block w-full border-gray-300 rounded-md shadow-sm" />
      </div>
      <button type="submit" className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 focus:outline-none focus:bg-blue-600">Upload</button>
      {/* <div>{loading && <img src="/loading.gif" alt="Loading..." />}</div> */}
    </form>
  </div>
  </div>
  );
};

export { FileUploader };
