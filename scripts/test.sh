echo "Running all tests"

./server/scripts/test.sh
./client/scripts/test.sh
./scripts/e2e.sh

echo 'All Tests have finished running'