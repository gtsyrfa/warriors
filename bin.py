class cl_test:
    def _notsoprivate(self):
        print("Not so private")
    
    def __soprivate(self):
        print("More private text")



tmp_var = cl_test()


tmp_var._notsoprivate()


tmp_var._cl_test__soprivate()
tmp_var._cl_test_notsoprivate()