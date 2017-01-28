

#calss header
class _DISTANT():
	def __init__(self,): 
		self.name = "DISTANT"
		self.definitions = [u'far away: ', u'part of your family but not closely related: ', u'far away in the past or future: ', u'quite soon: ', u'used to describe someone who does not show much emotion and is not friendly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
