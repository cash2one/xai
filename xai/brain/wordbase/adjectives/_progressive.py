

#calss header
class _PROGRESSIVE():
	def __init__(self,): 
		self.name = "PROGRESSIVE"
		self.definitions = [u'developing or happening gradually: ', u'Progressive ideas or systems are new and modern, encouraging change in society or in the way that things are done: ', u'A progressive tax system is one in which the rate of tax is higher on larger amounts of money.', u'The progressive form of a verb is used to show that the action is continuing. It is formed with the verb "be" followed by the present participle (= -ing form of the verb): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
