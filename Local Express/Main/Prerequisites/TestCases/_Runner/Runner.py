from Main.Prerequisites.TestCases.DeliveryOrder.DeliveryOrder import *
from Main.Prerequisites.TestCases.SignIn.LogInMarketplace import *
import os

reportDir = os.getcwd()

deliveryOrder_test = unittest.TestLoader().loadTestsFromTestCase(DeleveryOrder)
sigIn_test = unittest.TestLoader().loadTestsFromTestCase(LogInMarketplace)

test_suite = unittest.TestSuite([deliveryOrder_test, sigIn_test])
outfile = open(reportDir + "\Reports\TestReport.txt", "w")

runner = HtmlTestRunner.HTMLTestRunner(stream=outfile)

runner.run(test_suite)

#.HTMLTestRunner(stream=outfile, title='Test Report', description='Smoke Tests')



#      smoke_test = unittest.TestSuite()
#      smoke_test.addTests([
  #          unittest.defaultTestLoader.loadTestsFromTestCase(TestCases.DeliveryOrder.DeliveryOrder),
  #          unittest.defaultTestLoader.loadTestsFromTestCase(TestCases.SignIn.LogInMarketplace)
  #      ])

  # runner1 = HtmlTestRunner.HTMLTestRunner(
  #     stream=outfile,
  #     title='Test Report',
  #     description='Smoke Tests'
  # )

  # runner1.run(smoke_test)

#if __name__ == '__main__':
#    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="RunReports", report_name="Report.html"))

