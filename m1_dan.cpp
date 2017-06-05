#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <dirent.h>
#include <sys/types.h>

using namespace std;

DIR *opendir(const char* name);

vector<string> return_files(const char* filepath, vector<string> extensions){
    DIR *dir;
    struct dirent *ent;
    vector<string> vect;
    int i, length;
    size_t found;
    char* file;

    if ((dir = opendir(filepath)) != NULL) {
      /* print all the files and directories within directory */
      while ((ent = readdir (dir)) != NULL) {
          file = ent->d_name;
          printf ("%s\n", file);
          for (i = 0; i < extensions.size(); i++)
            found = string(file).find(extensions.at(i));
            if(found != string::npos) {
                vect.push_back(file);
            }
      }
      closedir (dir);
    } else {
      perror ("Could not open directory");
    }
    return vect;
}

string get_directory(){
    string directory;
    cout << "Input directory of library: ";
    getline(cin, directory);
    return directory;
}

vector<string> get_extensions(){
    int i;

    string extensions;
    cout << "Input extensions to import: ";
    getline(cin, extensions);
    cout << "Extensions: " << extensions << endl;

    vector<string> result;
    stringstream ss(extensions);

    while(ss.good()) {
        string substr;
        getline( ss, substr, ',' );
        result.push_back( substr );
    }

    return result;
}

int main()
{
    int i;
    //string directory = get_directory();
    vector<string> extensions = get_extensions();
    const char* path = "/Users/danlee/GitHub/SM_Music_POC/dan";
    vector<string> files = return_files(path, extensions);

    return 0;
}
