##encoding=UTF8

"""
C# make use of Python code:

I highly recommend Standard output method.

1. Standard output
    run python script from shell command line in C#. Use json string as a medium to pass data 
    between C# and Python
    
    advantage: easy to understand and fully compatible with python2, python3, no edit need in
               Python script
    
    negative: complex variable like Class, nested dictionary, data table is hard to parse

Here's a sample code to use in C#

    /*Study on Python Csharp Integration
     */
    [TestMethod]
    public void RunPython01()
    {
        // === initialize a ProcessStartInfo object ===
        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = @"C:\Python33\python3.exe";
        start.Arguments = string.Format("{0} {1}", @"C:\Users\shu\Documents\PythonWorkSpace\py3\py33_projects\Csharp_and_python_integration\sln01_standardIO.py", "");
        start.UseShellExecute = false;
        start.RedirectStandardOutput = true;

        using (Process process = Process.Start(start)) // run the process
        {
            using (StreamReader reader = process.StandardOutput) // read standard output
            {
                string result = reader.ReadToEnd();
                // Then you can use Json Deserializer to read data from 'string result'
                // put your code here...



            }
        }
    }

2. IronPython
    advantage: rich API is available in C# and also IronPython can call code, variable from both end.
    
    negative: many powerful extensions are not supported
"""

import json

def test():
    data = {"name": "sanhe", "title": "Data Scientist"}
    jsonstring = json.dumps(data, sort_keys=True, indent=4, separators=("," , ": "))
    print(jsonstring)
    
if __name__ == "__main__":
    test()