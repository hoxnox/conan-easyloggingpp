#include "easylogging++.h"

INITIALIZE_EASYLOGGINGPP

int main(int argc, char* argv[])
{
	LOG(INFO) << "test";
	return 0;
}

