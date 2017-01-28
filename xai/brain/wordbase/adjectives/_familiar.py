

#calss header
class _FAMILIAR():
	def __init__(self,): 
		self.name = "FAMILIAR"
		self.definitions = [u'easy to recognize because of being seen, met, heard, etc. before: ', u'to know something or someone well: ', u'informal and friendly, sometimes in a way that does not show respect to someone who is not a family member or close friend: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
