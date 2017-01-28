

#calss header
class _STEADY():
	def __init__(self,): 
		self.name = "STEADY"
		self.definitions = [u'happening in a smooth, gradual, and regular way, not suddenly or unexpectedly: ', u'not moving or changing suddenly: ', u'work that is likely to continue for a long time and for which you will be paid regularly: ', u'under control: ', u'used to describe someone who can be trusted to show good judgment and act in a reasonable way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
