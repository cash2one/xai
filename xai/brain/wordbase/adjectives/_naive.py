

#calss header
class _NAIVE():
	def __init__(self,): 
		self.name = "NAIVE"
		self.definitions = [u"too willing to believe that someone is telling the truth, that people's intentions in general are good, or that life is simple and fair. People are often naive because they are young and/or have not had much experience of life: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
