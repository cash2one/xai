

#calss header
class _NATIVE():
	def __init__(self,): 
		self.name = "NATIVE"
		self.definitions = [u"relating to or describing someone's country or place of birth or someone who was born in a particular country or place: ", u'used to refer to plants and animals that grow naturally in a place, and have not been brought there from somewhere else: ', u'relating to the first people to live in an area: ', u'the first language that you learn: ', u'A native ability or characteristic is one that a person or thing has naturally and is part of their basic character: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
