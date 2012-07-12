#include "requests.pb.cc"

#include <iostream>

using namespace std;

int main() {
  req::Request r;

  // Add the tagging extension.
  // r.MutableExtension(req::TaggingRequest::tagging);
  // both work because Clear() affects the content of the extension and not
  // that of `r'
  r.MutableExtension(req::TaggingRequest::tagging)->Clear();
  cout << "has tagging extension " << r.HasExtension(req::TaggingRequest::tagging) << endl;
  
  // Add the numbered extension and set its `number' field.
  req::NumberedRequest* numbered = r.MutableExtension(req::NumberedRequest::numbered);
  cout << "has numbered extension "
       << r.HasExtension(req::NumberedRequest::numbered) << endl;
  numbered->set_number(42);
  cout << "NumberedRequest field "
       << ((r.GetExtension(req::NumberedRequest::numbered)).number()) << endl;
}
