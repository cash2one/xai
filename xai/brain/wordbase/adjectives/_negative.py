

#calss header
class _NEGATIVE():
	def __init__(self,): 
		self.name = "NEGATIVE"
		self.definitions = [u'expressing "no": ', u'A negative sentence or phrase is one that contains a word such as "not", "no", "never", or "nothing": ', u'not expecting good things, or likely to consider only the bad side of a situation: ', u'bad or harmful: ', u'of the type of electrical charge that is carried by electrons', u'(of a medical test) showing that the patient does not have the disease or condition for which he or she has been tested: ', u'(of a number or amount) less than zero: ', u'not having the rhesus factor in the blood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
