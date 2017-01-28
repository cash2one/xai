

#calss header
class _NOW():
	def __init__(self,): 
		self.name = "NOW"
		self.definitions = [u'at the present time, not in the past or future: ', u'immediately: ', u'used to express how long something has been happening, from when it began to the present time: ', u'used in stories or reports of past events to describe a new situation or event: ', u'used when describing a situation that is the result of what someone just said or did: ', u'very soon: ', u'used to introduce a new subject: ', u'used in statements and questions to introduce or give emphasis to what you are saying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
