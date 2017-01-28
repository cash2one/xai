

#calss header
class _NAUGHTY():
	def __init__(self,): 
		self.name = "NAUGHTY"
		self.definitions = [u'When children are naughty, or their behaviour is naughty, they behave badly or do not do what they are told to do: ', u"used slightly humorously to describe an adult who has behaved badly or an adult's bad action: ", u'involving or suggesting sex: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
