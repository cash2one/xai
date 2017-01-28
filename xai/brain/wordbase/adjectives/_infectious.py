

#calss header
class _INFECTIOUS():
	def __init__(self,): 
		self.name = "INFECTIOUS"
		self.definitions = [u'(of a disease) able to be passed one person, animal, or plant to another: ', u'able to pass a disease from one person, animal, or plant to another: ', u'Something that is infectious has an effect on everyone who is present and makes them want to join in: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
