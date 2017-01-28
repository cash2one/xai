

#calss header
class _ACUTE():
	def __init__(self,): 
		self.name = "ACUTE"
		self.definitions = [u'If a bad situation is acute, it causes severe problems or damage: ', u'An acute pain or illness is one that quickly becomes very severe: ', u'used to describe intelligence, senses, etc. that are very good, accurate, and able to notice very small differences: ', u'An acute angle is less than 90 degrees.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
