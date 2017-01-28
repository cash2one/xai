

#calss header
class _INNOCENT():
	def __init__(self,): 
		self.name = "INNOCENT"
		self.definitions = [u'(of a person) not guilty of a particular crime: ', u'having no knowledge of the unpleasant and evil things in life: ', u'An innocent person is someone who is not involved with any military group or war: ', u'(of a thing) not intended to harm anyone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
