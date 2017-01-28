

#calss header
class _HORNY():
	def __init__(self,): 
		self.name = "HORNY"
		self.definitions = [u'sexually excited: ', u'sexually attractive: ', u'made of a hard substance, like horn: ', u'(especially of skin) hard and rough']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
