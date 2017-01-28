

#calss header
class _MASTOID():
	def __init__(self,): 
		self.name = "MASTOID"
		self.definitions = [u'relating to the mastoid process (= part of the skull just behind the ear): ', u'shaped like a breast or a nipple (= one of the two small darker parts that stick out from the breasts or chest)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
