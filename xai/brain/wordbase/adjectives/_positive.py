

#calss header
class _POSITIVE():
	def __init__(self,): 
		self.name = "POSITIVE"
		self.definitions = [u'full of hope and confidence, or giving cause for hope and confidence: ', u'certain and without any doubt: ', u'(of a medical test) showing that a person has the disease or condition for which they are being tested: ', u'(used to add force to an expression) complete: ', u'(of a number or amount) more than zero: ', u'being the type of electrical charge that is carried by protons', u'having the rhesus factor in the blood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
