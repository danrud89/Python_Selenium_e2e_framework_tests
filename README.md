# Tests

End-to-end testing with selenium and pytest.

## Install

1. Create and activate the python virtual environment

```bash
cd your_default__project_patch
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

### Run all tests (executed one by one)

```bash
pytest
```
### Run all tests parallel (in provided case 'n' means 5 parallel)

```bash
pytest n=5
```

### Run single test

```bash
pytest default_test_case_name.py 
```