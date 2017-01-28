

#calss header
class _SUSCEPTIBLE():
	def __init__(self,): 
		self.name = "SUSCEPTIBLE"
		self.definitions = [u'easily influenced or harmed by something: ', u'used to describe someone who is easily emotionally influenced: ', u'(especially of an idea or statement) able to be understood, proved, explained, etc. in a particular way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
